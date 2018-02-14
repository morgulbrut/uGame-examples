import stage
import ugame

PALETTE = (b'\xf0\x0f\x00\x00\xcey\xff\xff\xf0\x0f\x00\x19\xfc\xe0\xfd\xe0'
           b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

game = stage.Stage(ugame.display, 12)
text = stage.Text(16, 16, palette=PALETTE)
game.layers = [text]

i = 0

for y in range(16):
    for x in range(16):
        text.char(x, y, chr(i))
        print(chr(i))
        i += 1
        
game.render_block()