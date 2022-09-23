# biggest={}
# txt_file=open('parentlinks.txt','r')
# file_content=txt_file.read()
# file_content=file_content.split('\n')
# file_content=[i for i in file_content if i]
# for line in file_content:
#     l=line.split('?letter=')
#     letter=l[1][0]
#     show=line.split('&show=')
#     if len(show) > 1:
#         val=int(show[1])
#         if biggest.get(letter):
#             if biggest[letter] < val:
#                 biggest[letter]=val
#         else:
#             biggest[letter]=val

# print(biggest)