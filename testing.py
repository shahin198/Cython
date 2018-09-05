import timeit
number=100000
cy = timeit.timeit('''example_cy.test(5)''',setup='import example_cy',number=100000)
py = timeit.timeit('''example_py.test(5)''',setup='import example_py', number=100000)

print(number," iterations")
print("Cy execution time: ",cy, "Py execution time: ",py)

print('Cython is {}x faster from Python'.format(py/cy))
