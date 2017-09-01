# Setup some variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print a couple stupid lines of text
print(x)
print(y)

# Print the stupid text again, using formatted strings and variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Perform the setup for an unworthy joke
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} "

# Print the joke
print(joke_evaluation.format(hilarious))

# Illustrate concatentation, as though we have no idea what that is
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
