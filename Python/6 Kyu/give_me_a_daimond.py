"""Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
Task

You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size."""


def diamond(n):
    r = ""
    if (n % 2 == 0) | (n < 0):
        return None
    for i in range(n):
        a = "*" * (i * 2 + 1) if i <= (n / 2) else "*" * ((n - i) * 2 - 1)
        r += " " * int((n - len(a)) / 2) + a + "\n"
    return r
