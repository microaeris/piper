from scipy.misc import imread
import pdb

im = imread("./wave/frame-4b-cut.png", flatten=True)
y = len(im)     # row
x = len(im[0])  # col
print(im)

# Convert image to binary
result_bin = ""
num_tiles = x / 8
for i in range(num_tiles):
    for k in range(y):  # height of tile # y
        result_bin += "0b"
        for j in range(8):  # width of tile # x
            pixel = im[k, j + i*8]  # row, col -> y, x
            result_bin += str(int(pixel / 255))
        result_bin += " "
print(result_bin)



# # Convert binary to hex
# result_hex = ""
# bin_len = len(result_bin)
# for i in range(bin_len / 8):
#     # binary string to decimal
#     temp = int(result_bin[i * 8:(i + 1) * 8], 2)
#     print(temp)

#     # Want temp to be a decimal value
#     result_hex += '0x{:02x} '.format(temp)
# print(result_hex)
