medium_quiz = """Epistomology is the study of __1__, the first systematic 
attempts to think about epistomology were done by the ancient __2__ over
2500 years ago! One of the major categories of epistomology that involves reason is called __3__. 
Another major category used by modern science is called __4__. And finally,
the third major category grounded in 
skepticism is called __5__. 
All of these are different ways in which we can advance our __1__."""

medium_answer = ["knowledge", "greeks", "rationalism", "empiricism", "nihilism"]

easy_quiz = """Moral philosophy is the study of what one __1__ to do. This is distinct from other categories of philosophy 
which study the way the world is, instead of how it __1__ to be. Aristotle was the first to attempt 
moral philosophy, creating what is known as __2__ ethics. He has since been followed by others, 
most famously Kants __3__ and Bentham's __4__!"""

easy_answer = ["ought", "virtue", "deontological", "utilitarianism"]

hard_quiz = """Political philosophy is was once called the __1__ science by Aristotle. It was seen the largest growth
and change over time starting with a primative form of the __2__ contract by Plato. Over time, political philosophers have
come up with many unique theories such as Augustine's idea to the city like __3__, or guided by the __4__ for Rousseau."""

hard_answer = ["master", "social", "heaven", "general will"]

def string_run(user_input, blank_num, quiz_text):
	"""
	Updates the text of the quiz paragraph with correct user answers. Takes correct guesses from the user and
	updates the text of the quiz with these answers as output. It returns this to run_game funciton to print and 
	store.
	"""
	replace_num = 0
	quiz_text = quiz_text.split()
	for word in quiz_text:
		replace_num += 1
		if "__"+str(blank_num)+"__" in word:
			word = word.replace("__"+str(blank_num)+"__", user_input)
			quiz_text[replace_num - 1] = word
			new_print = " ".join(quiz_text)
	return new_print

def check_answer(answer, correct_answer,blank_num):
	"""
	Checks to see if user guess is correct or false. Takes user guess, the correct answer, and the current question
	number as input and tells the user if he is correct and returns either true or nothing to run_game function. 
	"""
	if answer == correct_answer[blank_num - 1]:
		print "\nCorrect! The paragraph now reads as:\n"
		return "true"	
 
def run_game(quiz_text,correct_answer,blank_num2):
	"""
	Main function. Takes user input and runs it through other functions keeping track of guesses and printing quiz after 
	correct guesses. Once the quiz has been completed or the number of tries exceded, this function returns to init_game 
	function.
	"""
	blank_num = 1
	wrong_num = 5
	while blank_num < blank_num2:
		print quiz_text
		if wrong_num == 0:
			print "\nGame Over. You missed too many times in a row. Lets try again!\n"
			blank_num = blank_num2
		else:	 
			user_input = (raw_input("\nWhat should we substitue for __" + str(blank_num)
			  + "__? \n").lower())
			answer_value = check_answer(user_input,correct_answer,blank_num)
			if answer_value == "true":
				wrong_num = 5
				quiz_text = string_run(user_input, blank_num, quiz_text)
				blank_num += 1
			else:
				wrong_num -= 1
				print "\nWrong. Chances left: " + str(wrong_num) + "\n"
	print quiz_text

def init_game(first_count):
	"""
	This allows user to choose the quiz they wish to take. It also allows user to choose to take another exam
	or leave the program. It outputs the text of the quiz, answers to the quiz, and number of answers to the 
	run_game function.
	"""
	while first_count == 0:
		user_input2 = raw_input("\nWould you like to attempt the easy, medium, or hard quiz? \n").lower()
		if user_input2 == "easy":
			first_count += 1
			run_game(easy_quiz,easy_answer,5)   	
		if user_input2 == "medium":
			first_count += 1 
			run_game(medium_quiz,medium_answer,6) 	 
		if user_input2 == "hard":
			first_count += 1
			run_game(hard_quiz, hard_answer, 5)
		if first_count == 0:
			print "\nIncorrect entry. please try again.\n" 
		if first_count == 1:
			user_input3 = raw_input("\nDo you want to play again? (y/n)\n").lower()
			if user_input3 == "y":
				first_count = 0		

init_game(0)
    				

