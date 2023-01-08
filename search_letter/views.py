from django.shortcuts import render

# Create your views here.
def search4letters(phrase:str, letters:str='aeiou') -> set:
	return set(letters).intersection(set(phrase))

def validate(request):
	if request.method == "POST":
		letter = request.POST['letter_input']
		phrase = request.POST['phrase_input']
		if letter == '':
			letter='aeiou'
		else:
			letter = request.POST['letter_input']
		result=search4letters(letter,phrase)
		result_list = list(result) 
		data = dict.fromkeys(result)
		
	return render(request,'validate.html',{'letter':letter,'phrase':phrase,'data':data})	

def Search4Phrase(request):
	return render(request, "letter_phrase.html")