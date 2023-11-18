student_num=15
leftover_blocks=[]
leftover_blocks_total=0
blue_block_num=int(input('enter the blue blocks number: '))
red_block_num=int(input('enter the blue red number: '))
green_block_num=int(input('enter the blue green number: '))
yellow_block_num=int(input('enter the blue yellow number: '))
leftover_blocks.append(blue_block_num%student_num)
leftover_blocks.append(red_block_num%student_num)
leftover_blocks.append(green_block_num%student_num)
leftover_blocks.append(yellow_block_num%student_num)
for i in leftover_blocks:
    leftover_blocks_total+=i

print(f'the total of the leftover blocks={leftover_blocks_total}')
print(f'the total of the blue blocks={leftover_blocks[0]}')
print(f'the total of the red blocks={leftover_blocks[1]}')
print(f'the total of the green blocks={leftover_blocks[2]}')
print(f'the total of the yellow blocks={leftover_blocks[3]}')





