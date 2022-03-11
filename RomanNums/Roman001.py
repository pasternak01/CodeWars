def solution(roman):
	romanNums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	year = 0
	prev_v = 0
	for i in roman:

		for k, v in romanNums.items():
			if i == k:
				if v > prev_v:
					year += v - (2 * prev_v)
				else:
					year += v
				prev_v = v
	return year




if __name__ == '__main__':
	print('Example')
	print(solution('MCMXC'))

# describe("Example Tests")
# assert_equals(solution('XXI'), 21, 'XXI should == 21')
# assert_equals(solution('I'), 1, 'I should == 1')
# assert_equals(solution('IV'), 4, 'IV should == 4')
# assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
