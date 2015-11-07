
# for testing cards.py

from cards import Deck

def main():
	d = Deck()
	for i in range(52):
		d.GetNextCard()

	exception_raised = False
	try:
		d.GetNextCard()
	except:
		exception_raised = True
	if not exception_raised:
		raise Exception('Error: dealing from empty deck did not raise exception')
	
	print 'tests passed'

if __name__ == "__main__":
    main()