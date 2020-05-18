#2048 By Tks

import argparse
import random
import os
import copy
import msvcrt
parser=argparse.ArgumentParser(description='2048 GAME by Tks')
parser.add_argument('--n',type=int, default=5, help='provide the grid size in integar (default : 5)')
parser.add_argument('--w',type=int, default=2048, help='provide an integar (default : 2048)')
args = parser.parse_args()
n = args.n
w = args.w

def check_zero(tlist):
	for i in range(n):
		if not tlist[i]==0:
			for m in range(i,n):
				if tlist[m]==0:
					return True

	return False

def check_equal(tlist):
	for i in range(n-1):
		if tlist[i]!=0 and tlist[i]==tlist[i+1]:
			return True
	return False

def r_zero(tlist):
	for i in list(reversed(range(n))):
		if tlist[i]==0:
			for k in list(reversed(range(i+1))):
				if k==0:
					tlist[k]=0
				elif not k==0:
					tlist[k]=tlist[k-1]
	return tlist

def add(tlist):
	for i in list(reversed(range(1,n))):
		if tlist[i]==tlist[i-1]:
			tlist[i]=tlist[i]+tlist[i-1]
			tlist[i-1]=0
	return tlist

def movement(tlist):
	
	while check_zero(tlist):
		tlist = r_zero(tlist)
	tlist = add(tlist)
	while check_zero(tlist):
		tlist = r_zero(tlist)
	
	return tlist

def input_result(game_map, key_input):
	#DOWN
	if key_input.lower()=='s':
		for j in range(n):
			tlist=[]
			for i in range(n):
				tlist.append(game_map[i][j])
			tlist=movement(tlist)
			for i in range(n):
				game_map[i][j]=tlist[i]
	#UP
	if key_input.lower()=='w':
		for j in range(n):
			tlist=[]
			for i in list(reversed(range(n))):
				tlist.append(game[i][j])
			tlist=movement(tlist)
			for i in range(n):
				game_map[n-1-i][j]=tlist[i]
	#LEFT
	if key_input.lower()=='a':
		for i in range(n):
			tlist=[]
			for j in list(reversed(range(n))):
				tlist.append(game_map[i][j])
			tlist=movement(tlist)
			for j in range(n):
				game_map[i][n-1-j]=tlist[j]
	#RIGHT
	if key_input.lower()=='d':
		for i in range(n):
			tlist=[]
			for j in range(n):
				tlist.append(game_map[i][j])
			tlist=movement(tlist)
			for j in range(n):
				game_map[i][j]=tlist[j]
	return game_map

def game_finish(game_map):
	for i in range(n):
		for j in range(n):
			if game_map[i][j]==w:
				print("Winner Winner Chicken Dinner!!! \n")
				return True
	if not zero_available(game_map) and game_equal(game_map):
		print("GAME OVER :( \n")
		return True
	return False
def zero_available(game_map):
	for i in range(n):
		for j in range(n):
			if game_map[i][j]==0:
				return True
	return False
def game_equal(game_map):
	for i in range(n):
		for j in range(n-1):
			if game_map[i][j]==game_map[i][j+1]:
				return False
	for j in range(n):
		for i in range(n-1):
			if game_map[i][j]==game_map[i+1][j]:
				return False
	return True
#MAIN CODE
play = True
while play:

	game = [[0 for i in range(n)] for i in range(n)]
	row1=random.randrange(n)
	col1=random.randrange(n)
	game[row1][col1]=2

	while True:
		row2=random.randrange(n)
		col2=random.randrange(n)
		if game[row2][col2]==0:
			game[row2][col2]=2
			break
	print("welcome to 2o48 By Tks")
	for row in game:
		print(row)
	print('Target to score: ', w)
	game_won=False
	while not game_won:
		tf1=True
		print('Please make a move(W/A/S/D): ')
		key_input= msvcrt.getch().decode("utf-8").lower()
		os.system('cls')
		if key_input in ['a', 'w', 's', 'd']:
			game1=copy.deepcopy(game)
			game = input_result(game, key_input)
			game2=copy.deepcopy(game)
			game_won= game_finish(game)
			if game1==game2 and not game_won:
				print('Wrong Move!(No tiles moved), make a move again \n')
				tf1=False
			while zero_available(game) and tf1:
				row=random.randrange(n)
				col=random.randrange(n)
				if game[row][col]==0:
					game[row][col]=2
					break
			for row in game:
				print(row)
		else :
			for row in game:
				print(row)
			print("sorry, wrong input! are you sure you entered A,S,W or D?? ")
	print(" ")
	tf=True
	while tf:
		choice = str(input("Do you want to play again? (Y or N): "))
		if choice.lower()=='n':
			play=False
			tf=False
			print(" ")
			print("Thanks for playing :)")
		elif choice.lower()=='y':
			print(" ")
			tf=False
		else:
			print("oops, Wrong input!")
			print(" ")




		





