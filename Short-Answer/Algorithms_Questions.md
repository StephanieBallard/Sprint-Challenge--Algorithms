# Analysis of Algorithms

## Exercise I

For this portion of the Sprint Challenge, you'll be answering questions posed in the `Algorithms_Questions.md` document inside the `Short-Answer` directory. Write down your answer and also write down a justification for _why_ you put down that answer. This could net you some partial credit if your justification is sound but the answer you put down turns out to not be correct. Add your answers to the questions in the `Algorithms_Answers.md` file.

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I think a naive approach would be to run through the array of floors and say ok for floor in the first index does the egg break and then keep going until the egg breaks and then know that we have found f.

A better approach might be to take the total of floors find the mid point and drop it there and if it doesn't break we know we can go higher, if it does break we know we can go lower. so then we can go to the mid point of that next range and see what happens to the egg and then that will give a new range to work through until we pin point our target floor.