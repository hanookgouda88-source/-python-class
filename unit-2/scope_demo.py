# Local variable shadows the global variable

count = 0


def tick_shadow():
    count = 0
    count += 1
    return count


print(tick_shadow(), tick_shadow(), count)


# Constant and function

THRESHOLD = 70


def is_alert(value):
    return value > THRESHOLD


print(is_alert(85), is_alert(60))


# Global variable

counter = 0


def tick_global():
    global counter
    counter += 1
    return counter


print(tick_global(), tick_global(), tick_global())

print("global counter is now:", counter)


# Updating value through return

def tick(n):
    return n + 1


total = 0

total = tick(total)
total = tick(total)

print("total:", total)