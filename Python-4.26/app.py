# employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines()[2])
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# ---------------------------------------------------------------

# employee_file = open("employees.txt", "a")
# employee_file = open("employees.txt", "w")
# employee_file.write("Tobey-Programmer")
# employee_file.write("\nKelly-Customer Service")
# employee_file.write("Tobey-Programmer")
# employee_file.close()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
from question import question

question_prompt =[
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

Questions=[
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b")
]