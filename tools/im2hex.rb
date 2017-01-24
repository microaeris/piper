require 'chunky_png'

image = ChunkyPNG::Image.from_file('./wave/1-5.png')

(0..image.dimension.height - 1).each do |y|
  tmp = ''
  (0..image.dimension.width - 1).each do |x|
    r = ChunkyPNG::Color.r(image[x,y])
    r == 255 ? tmp.prepend('1') : tmp.prepend('0')
  end

  i = 0
  while i < 56
     print "0x%02X" % tmp[i...i+8].to_i(2)
     print " "
     i += 8
  end

end

print "\n"