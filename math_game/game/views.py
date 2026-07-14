from django.shortcuts import render, redirect
import random


def play_game(request):
    # ئەگەر ئويۇن يېڭى باشلانغان بولسا، سەھىپىنى نۆللەيمىز
    if 'score' not in request.session:
        request.session['score'] = 0
        request.session['level'] = 1

    score = request.session['score']
    level = request.session['level']
    message = ""

    # جاۋاب يوللانغان بولسا تەكشۈرۈش
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        correct_answer = request.session.get('correct_answer')

        try:
            if int(user_answer) == int(correct_answer):
                request.session['score'] += 1
                # ھەر 3 نومۇردا بىر قىيىنلىق دەرىجىسى ئۆسىدۇ
                request.session['level'] = (request.session['score'] // 3) + 1
                message = "Correct"
            else:
                message = "Wrong"
                # خاتا تاپسا نومۇر نۆللىنىپ، 1-دەرىجىگە چۈشىدۇ
                request.session['score'] = 0
                request.session['level'] = 1
        except (ValueError, TypeError):
            message = "Wrong"

        # يېڭى بىر سوئال تۈزۈش ئۈچۈن بەتنى يېڭىلايمىز
        request.session.modified = True
        return redirect('play_game')

    # قىيىنلىق دەرىجىسىگە ئاساسەن سانلار دەرىجىسىنى بەلگىلەش
    # 1-دەرىجە: 1-10 غىچە سانلارنى قوشۇش
    # دەرىجە ئاشقانسېرى سانلار چوڭىيىدۇ ۋە كۆپەيتىش، ئېلىشلار قوشۇلىدۇ
    max_num = level * 10
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)

    operators = ['+']
    if level > 1:
        operators.append('-')
    if level > 2:
        operators.append('*')

    operator = random.choice(operators)

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        # مەنپىي سان چىقىپ قالماسلىق ئۈچۈن چوڭىنى ئالدىغا قويىمىز
        if num1 < num2:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
    elif operator == '*':
        # كۆپەيتىشتە سانلار بەك چوڭ بولۇپ كەتمەسلىك ئۈچۈن چەكلەيمىز
        num1 = random.randint(1, min(max_num, 12))
        num2 = random.randint(1, min(max_num, 12))
        correct_answer = num1 * num2

    # جاۋابنى سىستېمىدا ساقلاپ تۇرىمىز
    request.session['correct_answer'] = correct_answer

    context = {
        'num1': num1,
        'num2': num2,
        'operator': operator,
        'score': score,
        'level': level,
        'message': message
    }
    return render(request, 'game/index.html', context)


def reset_game(request):
    request.session['score'] = 0
    request.session['level'] = 1
    return redirect('play_game')