""""
# 1.selective_statements
# if_condition:
# if_condition:
# else:
#
# if_we_want_to_test_three_conditions_then_use_if_elif_else
# example: traffic_signals
# green_yellow_red
print('please select your choice:\n1.green\n2.red\n3.yellow')
color = input('color:')
if color == 'green':
    print('go safe, and drive safe')
elif color == 'red':
    print('stop')
else:
    print('wait for a minute and go')
    """
"""
# elif_ladder: multiple_conditions_if_we_want_to_test_then_we_need_multiple_elif
# example: hotel_Use_case
#
item = input('Enter your choice:')
if item == 'biryani':
    print('enjoy')
elif item == 'veg pulav':
    print('delicious')
elif item == 'Idli':
    print('yummy')
elif item == 'vadapav':
    print('ohhkk')
elif item == 'nimbu pani':
    print('thik hai')
else:
    print('bhai pani')
"""
Budget = int(input('enter your budget:'))
if Budget >= 50000:
    brand = input('enter