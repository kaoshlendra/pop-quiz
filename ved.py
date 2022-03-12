correct_ans = 0
incorrect_ans = 0
print('\n')
print('welcome to quiz\n ')
print('1) start')
print('2) exit')
Game_state = raw_input('\n')
if(Game_state == 'start' or Game_state == '1' or Game_state =='Start'):
 print('\n')
 print("1) Which animal is the national bird of India ?")
 print("a) Peacock  b) HummingBird  c) Ostrich  d) Sparrow")
 answer =raw_input()
 
 if(answer==answer=='a'  or answer =='peacock' or answer == 'Peacock'):
    print('correct answer\n ')
    correct_ans+=1
 else:
    print('wrong answer\n ')
    incorrect_ans+=1

 print("2) How many colors are there on the Indian Flag ?")
 print("a) 2  b) 5  c) 3  d) 1")
 answer =raw_input()
 
 if(answer=='c'  or answer =='3' ):
     print('correct answer\n ')
     correct_ans+=1
 else:
     print('wrong answer\n ')
     incorrect_ans+=1

 print("3) What is the capital of India ?")
 print("a) Mumbai  b) New Delhi  c) Bangalore  d) Chennai")
 answer =raw_input()

 if (answer == 'b'  or answer =='new delhi' or answer == '2' or answer == 'New Delhi'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n ')
     incorrect_ans += 1
 
 print("4) How many states are there in India ?")
 print("a) 29  b) 25  c) 30  d) 27")
 answer =raw_input()
 
 if (answer == 'a'  or answer =='29' or answer == '1'):
     print('correct answer\n ')
     correct_ans += 1
 else:
    print('wrong answer\n ')
    incorrect_ans += 1

 print("5) How many union territories are there in India ?")
 print("a) 5  b) 10  c) 8  d) 7")
 answer =raw_input()
 
 if (answer == 'd'  or answer =='7' or answer == '4'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n ')
     incorrect_ans += 1

 print("6) Which is the smallest state in India ?")
 print("a) Bihar  b) Kerela  c) Goa  d) Haryana")
 answer =raw_input()

 if (answer == 'c'  or answer =='goa' or answer == '3' or answer == 'Goa'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n ')
     incorrect_ans += 1

 print("7) Which animal is the national animal of India ?")
 print("a) Lion  b) Elephant  c) Tiger  d) Bear")
 answer =raw_input()

 if (answer == 'c' or answer =='tiger' or answer == 'Tiger' or answer == '3'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n ')
     incorrect_ans += 1

 print("8) Which is the biggest state in India ?")
 print("a) Rajasthan  b) Madhya Pradesh  c) Uttar Pradesh  d) Maharashtra")
 answer =raw_input()

 if (answer == 'a'  or answer =='Rajasthan' or answer == '1' or answer == 'rajasthan'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n ')
     incorrect_ans += 1
    
 print("9) Which is the National Sport of India ?")
 print("a) Cricket  b) Volleyball  c) Basketball  d) Hockey")
 answer =raw_input()

 if (answer == 'd'  or answer =='hockey' or answer == '4' or answer == 'Hockey'):
     print('correct answer\n')
     correct_ans += 1
 else:
     print('wrong answer\n')
     incorrect_ans += 1
    
 print("10) Who is the current Prime Minister of India ?")
 print("a) Amit Shah  b) Narendra Modi  c) Rajnath Singh  d) Yogi Adityanath")
 answer =raw_input()

 if (answer == 'b'  or answer =='Narendra Modi' or answer == '1' or answer =='narendra modi'):
     print('correct answer\n ')
     correct_ans += 1
 else:
     print('wrong answer\n')
     incorrect_ans += 1
    
 print("Number of correct answers:")
 print(correct_ans)
 print("Number of incorrect answers:")
 print(incorrect_ans)

else:
   print('\n')
   print('thank you') 