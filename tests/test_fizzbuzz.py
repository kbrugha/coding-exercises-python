import filecmp
import subprocess
from src.exercises.fizzbuzz import get_fizzbuzz, fizzbuzz


def test_fizzbuzz():
    mod_list = {3: "Fizz", 5: 'Buzz'}

    assert get_fizzbuzz(3, mod_list) == "Fizz"
    assert get_fizzbuzz(5, mod_list) == "Buzz"
    assert get_fizzbuzz(15, mod_list) == "FizzBuzz"


def test_threefive(capfd):
    mod_list = {3: "Three", 5: 'Five'}

    fizzbuzz(10, mod_list)
    out, _ = capfd.readouterr()
    assert out == "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n"


def test_cmd_defaults():
    command = "src/exercises/fizzbuzz.py"

    with open("actual_fizzbuzz.txt", "w", encoding='utf-8') as file:
        subprocess.run(command, check=True, stdout=file)

    expected_fizzbuzz = "tests/expected_fizzbuzz.txt"
    actual_fizzbuzz = "actual_fizzbuzz.txt"

    result = filecmp.cmp(expected_fizzbuzz, actual_fizzbuzz, shallow=False)
    assert result is True


def test_cmd_options():
    command = ["src/exercises/fizzbuzz.py",
               "--length=15", "--mod", "3=Fizz", "5=Buzz"]

    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)

    assert result.stdout.decode(
        'UTF-8') == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n"


if __name__ == "__main__":
    pass
