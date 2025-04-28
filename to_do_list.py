def add_list():
	add_task = input("Enter your task::")
	with open("list_task.txt",'a') as f:
		f.write(add_task + '\n')


def view_list():
	with open("list_task.txt","r") as r:
		read =r.readline()
		print(read)


def mark_done():
	mark_task = input("Enter the task you want to mark done:: ")
	with open("list_task.txt","a") as m:
		m.remove(mark_task)


def left_list():
	with open("list_task.txt","r") as l:
		lisst = l.readline()
		print(lisst)

'''This program contains the code of the TO_DO_LIST'''

print('!!!!!!!!!!!!!!! Hello! Welcome. !!!!!!!!!!!!!!!!!')
print("Here you can keep the records of your tasks.")

Name = input("Enter your Name:: ")
Age = int(input("Enter your age:: "))

print("Press 1 to add task in list.\nPress 2 to view task of list.\nPress 3 to mark done to task.\n Press 4 to see the rest of task.\n Press 5 to quit()")

while True:
	choice = int(input("Enter your choice from (1 to 5):: "))
	if choice == 1:
		add_list()
	elif choice == 2:
		view_list()
	elif choice == 3:
		mark_done()
	elif choice == 4:
		left_list()
	elif choice == 5:
		break
	else:
		print("Inavlid choice !")