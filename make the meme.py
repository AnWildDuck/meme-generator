from pygame import *
import random, glob


# Get meme templates
files = glob.glob('templates\\*')
templates = []

for file in files:
    img = image.load(file)
    templates.append(img)


# Get text
file = open('text.txt', 'r').read().splitlines()
last = []
sayings = []

for line in file:
    
    if line == '':
        sayings.append(last)
        last = []
    else:
        last.append(line)

sayings.append(last)
        

# Get batch size
while True:
    print()
    amount = input('How many memes sir?: ')

    try:
        amount = int(amount)
        break
    
    except:
        print('A number please')
        print()


# Make the memes
font.init()
my_font = font.SysFont('tahoma', 30)
margin = 5
img_width = 500

for meme_num in range(amount):

    img = random.choice(templates)
    saying = random.choice(sayings)

    message_height = margin
    message_width = 0
    messages = []
    line_heights = []

    for line in saying:
        message = my_font.render(line, 0, (0, 0, 0))
        messages.append(message)
        rect = message.get_rect()
        message_height += (rect.height + margin)
        message_width = max(message_width, rect.width)
        line_heights.append(rect.height)

    line_height = sum(line_heights) / len(line_heights)
    img_rect = img.get_rect()
    
    # Scale img to standard size
    scale = img_width / img_rect.width
    img = transform.scale(img, (int(img_width), int(img_rect.height * scale)))
    img_rect = img.get_rect()

    message_width += margin * 2
    
    height = message_height + img_rect.height
    width = max(message_width, img_rect.width + margin * 2)

    # Make surface
    main = Surface((width, height))
    main.fill((255, 255, 255))

    # Add messages to the surface
    for mes_index in range(len(messages)):
        message = messages[mes_index]

        y = margin + mes_index * (line_height + margin)
        main.blit(message, (margin, y))

    # Add the image to the surface
    main.blit(img, (margin, height - img_rect.height))

    # Save the meme
    numbers_used = glob.glob('memes\\meme(*).png')
    numbers_used = [int(x[11:len(x) - 5]) for x in numbers_used]

    if len(numbers_used) > 0: next_num = max(numbers_used) + 1
    else: next_num = 0

    image.save(main, 'memes\\meme(' + str(next_num) + ').png')
