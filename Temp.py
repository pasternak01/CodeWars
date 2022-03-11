def array_diff(a, b):
	# return [i for i in a for ii in b if i != ii if len(b) >= 1] if len(b) >= 1 else a
	# return list(set(a) - set(b)) if len(b) >= 1 else a

	return [i for i in a if i not in b] if len(b) >= 1 else a



print(array_diff([1 ,2 ,3], [1, 2]))
# z = [1]
# print(z[0] == 1)


# def basic_test_cases():
# 	test.assert_equals(array_diff([1 ,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
# 	test.assert_equals(array_diff([1 ,2 ,2], [1]), [2 ,2], "a was [1,2,2], b was [1], expected [2,2]")
# 	test.assert_equals(array_diff([1 ,2 ,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
# 	test.assert_equals(array_diff([1 ,2 ,2], []), [1 ,2 ,2], "a was [1,2,2], b was [], expected [1,2,2]")
# 	test.assert_equals(array_diff([], [1 ,2]), [], "a was [], b was [1,2], expected []")
# 	test.assert_equals(array_diff([1 ,2 ,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")
