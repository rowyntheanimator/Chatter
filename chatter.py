import pygame


CHATTER_VIR = 4.1

CHATTER_TITLE_NAME = "Iso"

def set_title_name(name):
    global CHATTER_TITLE_NAME
    CHATTER_TITLE_NAME = name

advance = 0





pygame.init()

CHATTER_WIDTH = 700
CHATTER_HEIGHT = 700


screen = pygame.display.set_mode((CHATTER_WIDTH, CHATTER_HEIGHT))
pygame.display.set_caption(CHATTER_TITLE_NAME)

PALETTE = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "red": (255, 0, 0),
    "dark_red": (139, 0, 0),
    "light_red": (255, 102, 102),
    "green": (0, 255, 0),
    "dark_green": (0, 100, 0),
    "light_green": (144, 238, 144),
    "blue": (0, 0, 255),
    "dark_blue": (0, 0, 139),
    "light_blue": (173, 216, 230),
    "cyan": (0, 255, 255),
    "dark_cyan": (0, 139, 139),
    "light_cyan": (224, 255, 255),
    "yellow": (255, 255, 0),
    "dark_yellow": (204, 204, 0),
    "light_yellow": (255, 255, 153),
}


for color_name, rgb in PALETTE.items():
    globals()[color_name] = rgb
def graphics(x, y, color, layer="dynamic"):
    """
    Set a pixel at (x, y) to a specific color (RGB) on the specified layer (static or dynamic).
    
    Args:
    - x (int): X coordinate on the screen.
    - y (int): Y coordinate on the screen.
    - color (tuple): A tuple of RGB values (r, g, b).
    - layer (str): Which layer to update ("static" or "dynamic").
    """
    if 0 <= x < CHATTER_WIDTH and 0 <= y < CHATTER_HEIGHT:
        # Choose the surface based on the layer argument
        if layer == "static":
            level_surface.set_at((int(x), int(y)), color)  # Modify static surface
        elif layer == "dynamic":
            dynamic_surface.set_at((int(x), int(y)), color)  # Modify dynamic surface
        else:
            print("Error: Invalid layer specified. Use 'static' or 'dynamic'.")


def display_screen():
    """
    Blits both the static and dynamic surfaces onto the screen and updates the display.
    """
    # First, blit the static surface (level) onto the screen
    screen.blit(level_surface, (0, 0))  # Static background or level
    
    # Then, blit the dynamic surface (moving objects) onto the screen
    screen.blit(dynamic_surface, (0, 0))  # Dynamic elements like player, enemies
    
    # Finally, update the display to show the new screen contents
    pygame.display.update()  # Or pygame.display.flip() if you want to flip the entire screen


def load_sprite(image_path):
    """
    Loads a sprite (image) from the given file path.
    Args:
    - image_path (str): The file path of the image to be loaded.
    
    Returns:
    - pygame.Surface: A Surface object representing the loaded image.
    """
    try:
        sprite = pygame.image.load(image_path)
        return sprite
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None

tile0 = load_sprite("tiles/0.png")
tile1 = load_sprite("tiles/1.png")
tile2 = load_sprite("tiles/2.png")
tile3 = load_sprite("tiles/3.png")
tile4 = load_sprite("tiles/4.png")
tile5 = load_sprite("tiles/5.png")
tile6 = load_sprite("tiles/6.png")
tile7 = load_sprite("tiles/7.png")
tile8 = load_sprite("tiles/8.png")
tile9 = load_sprite("tiles/9.png")
tile10 = load_sprite("tiles/10.png")
tile11 = load_sprite("tiles/11.png")
tile12 = load_sprite("tiles/12.png")
tile13 = load_sprite("tiles/13.png")
tile14 = load_sprite("tiles/14.png")
tile15 = load_sprite("tiles/15.png")
tile16 = load_sprite("tiles/16.png")
tile17 = load_sprite("tiles/17.png")
tile18 = load_sprite("tiles/18.png")
tile19 = load_sprite("tiles/19.png")
tile20 = load_sprite("tiles/20.png")
tile21 = load_sprite("tiles/21.png")
tile22 = load_sprite("tiles/22.png")
tile23 = load_sprite("tiles/23.png")
tile24 = load_sprite("tiles/24.png")
tile25 = load_sprite("tiles/25.png")
tile26 = load_sprite("tiles/26.png")
tile27 = load_sprite("tiles/27.png")
tile28 = load_sprite("tiles/28.png")
tile29 = load_sprite("tiles/29.png")
tile30 = load_sprite("tiles/30.png")
tile31 = load_sprite("tiles/31.png")
tile32 = load_sprite("tiles/32.png")
tile33 = load_sprite("tiles/33.png")
tile34 = load_sprite("tiles/34.png")
tile35 = load_sprite("tiles/35.png")
tile36 = load_sprite("tiles/36.png")
tile37 = load_sprite("tiles/37.png")
tile38 = load_sprite("tiles/38.png")
tile39 = load_sprite("tiles/39.png")
tile40 = load_sprite("tiles/40.png")
tile41 = load_sprite("tiles/41.png")
tile42 = load_sprite("tiles/42.png")
tile43 = load_sprite("tiles/43.png")
tile44 = load_sprite("tiles/44.png")
tile45 = load_sprite("tiles/45.png")
tile46 = load_sprite("tiles/46.png")
tile47 = load_sprite("tiles/47.png")
tile48 = load_sprite("tiles/48.png")
tile49 = load_sprite("tiles/49.png")
tile50 = load_sprite("tiles/50.png")
tile51 = load_sprite("tiles/51.png")
tile52 = load_sprite("tiles/52.png")
tile53 = load_sprite("tiles/53.png")
tile54 = load_sprite("tiles/54.png")
tile55 = load_sprite("tiles/55.png")
tile56 = load_sprite("tiles/56.png")
tile57 = load_sprite("tiles/57.png")
tile58 = load_sprite("tiles/58.png")
tile59 = load_sprite("tiles/59.png")
tile60 = load_sprite("tiles/60.png")
tile61 = load_sprite("tiles/61.png")
tile62 = load_sprite("tiles/62.png")
tile63 = load_sprite("tiles/63.png")
tile64 = load_sprite("tiles/64.png")
tile65 = load_sprite("tiles/65.png")
tile66 = load_sprite("tiles/66.png")
tile67 = load_sprite("tiles/67.png")
tile68 = load_sprite("tiles/68.png")
tile69 = load_sprite("tiles/69.png")
tile70 = load_sprite("tiles/70.png")
tile71 = load_sprite("tiles/71.png")
tile72 = load_sprite("tiles/72.png")
tile73 = load_sprite("tiles/73.png")
tile74 = load_sprite("tiles/74.png")
tile75 = load_sprite("tiles/75.png")
tile76 = load_sprite("tiles/76.png")
tile77 = load_sprite("tiles/77.png")
tile78 = load_sprite("tiles/78.png")
tile79 = load_sprite("tiles/79.png")
tile80 = load_sprite("tiles/80.png")
tile81 = load_sprite("tiles/81.png")
tile82 = load_sprite("tiles/82.png")
tile83 = load_sprite("tiles/83.png")
tile84 = load_sprite("tiles/84.png")
tile85 = load_sprite("tiles/85.png")
tile86 = load_sprite("tiles/86.png")
tile87 = load_sprite("tiles/87.png")
tile88 = load_sprite("tiles/88.png")
tile89 = load_sprite("tiles/89.png")
tile90 = load_sprite("tiles/90.png")
tile91 = load_sprite("tiles/91.png")
tile92 = load_sprite("tiles/92.png")
tile93 = load_sprite("tiles/93.png")
tile94 = load_sprite("tiles/94.png")
tile95 = load_sprite("tiles/95.png")
tile96 = load_sprite("tiles/96.png")
tile97 = load_sprite("tiles/97.png")
tile98 = load_sprite("tiles/98.png")
tile99 = load_sprite("tiles/99.png")
tile100 = load_sprite("tiles/100.png")
tile101 = load_sprite("tiles/101.png")
tile102 = load_sprite("tiles/102.png")
tile103 = load_sprite("tiles/103.png")
tile104 = load_sprite("tiles/104.png")
tile105 = load_sprite("tiles/105.png")
tile106 = load_sprite("tiles/106.png")
tile107 = load_sprite("tiles/107.png")
tile108 = load_sprite("tiles/108.png")

font_map = {
    'A': tile0,
    'B': tile1,
    'C': tile2,
    'D': tile3,
    'E': tile4,
    'F': tile5,
    'G': tile6,
    'H': tile7,
    'I': tile8,
    'J': tile9,
    'K': tile10,
    'L': tile11,
    'M': tile12,
    'N': tile13,
    'O': tile14,
    'P': tile15,
    'Q': tile16,
    'R': tile17,
    'S': tile18,
    'T': tile19,
    'U': tile20,
    'V': tile21,
    'W': tile22,
    'X': tile23,
    'Y': tile24,
    'Z': tile25,
    'a': tile26,
    'b': tile27,
    'c': tile28,
    'd': tile29,
    'e': tile30,
    'f': tile31,
    'g': tile32,
    'h': tile33,
    'i': tile34,
    'j': tile35,
    'k': tile36,
    'l': tile37,
    'm': tile38,
    'n': tile39,
    'o': tile40,
    'p': tile41,
    'q': tile42,
    'r': tile43,
    's': tile44,
    't': tile45,
    'u': tile46,
    'v': tile47,
    'w': tile48,
    'x': tile49,
    'y': tile50,
    'z': tile51,
    '0': tile61,
    '1': tile52,
    '2': tile53,
    '3': tile54,
    '4': tile55,
    '5': tile56,
    '6': tile57,
    '7': tile58,
    '8': tile59,
    '9': tile60,
    '!': tile62,
    '@': tile63,
    '#': tile64,
    '$': tile65,
    '%': tile66,
    '^': tile67,
    '&': tile68,
    '*': tile69,
    '(': tile70,
    ')': tile71,
    '-': tile72,
    '_': tile73,
    '+': tile74,
    '=': tile75,
    '[': tile76,
    ']': tile77,
    '{': tile78,
    '}': tile79,
    '|': tile80,
    '\\': tile81,
    ';': tile82,
    ':': tile83,
    '\'': tile84,
    '\"': tile85,
    ',': tile86,
    '.': tile87,
    '<': tile88,
    '>': tile89,
    '/': tile90,
    '?': tile91,
    '`': tile92,
    '~': tile93,
    '░': tile94,
    '▓': tile95,
    '█': tile96,
    '│': tile97,
    '─': tile98,
    '└': tile99,
    '┘': tile100,
    '┐': tile101,
    '┌': tile102,
    '├': tile103,
    '┤': tile104,
    '┴': tile105,
    '┼': tile106,
    '┬': tile107,
    ' ': tile108,
}

def tint(surface, color):
    # Create a new surface with same size, with SRCALPHA
    tinted = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    # Fill with color, zero alpha so original alpha is kept
    tinted.fill(color + (0,))
    # Blit the original glyph on top — alpha is preserved
    tinted.blit(surface, (0, 0))
    return tinted



def display_sprite(sprite, x, y, scale=1, layer="dynamic", tint=None):
    """
    Displays a sprite at the specified coordinates on the specified layer, with optional scaling and tinting.

    Args:
    - sprite (pygame.Surface): The sprite (image) to be displayed.
    - x (int): The x-coordinate where the sprite should be placed.
    - y (int): The y-coordinate where the sprite should be placed.
    - scale (int): The factor by which the sprite should be scaled (default is 1, meaning no scaling).
    - layer (str): The layer on which to display the sprite ("static" or "dynamic"). Default is "dynamic".
    - tint (tuple or pygame.Color, optional): RGB(A) color to tint the sprite. Example: (255, 0, 0, 128)
    """
    if not sprite:
        return

    if scale != 1:
        width = max(1, int(sprite.get_width() * scale))
        height = max(1, int(sprite.get_height() * scale))
        # Use plain scale for sharp edges
        scaled_sprite = pygame.transform.scale(sprite, (width, height))
    else:
        scaled_sprite = sprite.copy()

    # Apply tint if provided
    if tint:
        # Make sure the surface has alpha for blending
        tinted_sprite = scaled_sprite.copy()
        overlay = pygame.Surface(tinted_sprite.get_size(), pygame.SRCALPHA)
        overlay.fill(tint)  # tint should be (R, G, B, A)
        tinted_sprite.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        scaled_sprite = tinted_sprite

    # Blit to the correct layer
    if layer == "static":
        level_surface.blit(scaled_sprite, (x, y))
    elif layer == "dynamic":
        dynamic_surface.blit(scaled_sprite, (x, y))
    else:
        print("Error: Invalid layer specified. Use 'static' or 'dynamic'.")


def display_character(x, y, char, color, scale=1):
    glyph = font_map[char]
    display_sprite(glyph, x, y, scale, tint=color)

    return 9 * scale

def display_text(x, y, text, color, scale=2):
    """
    Displays text at the specified coordinates with specified color and scale.

    Args:
    - x (int): The x-coordinate where the text should be placed.
    - y (int): The y-coordinate where the text should be placed.
    - text (str): The text to be displayed (see lines 212-320 to see the char map).
    - color (tuple): The color of which to display the text with (formatted (R, G, B)).
    - scale (int): The factor by which the test should be scaled.
    """
    posE = x
    position = x
    positiony = y

    for char in text:
        if char == "\n":
            positiony += 9 * scale
            position = posE
        else:
            advance = display_character(position, positiony, char, color, scale)
            position += advance



def display_line(x1, y1, x2, y2, color, layer="dynamic"):
    """
    Draw a line from (x1, y1) to (x2, y2) with the given color on the specified layer.
    
    Args:
    - x1, y1 (int): Starting point of the line.
    - x2, y2 (int): Ending point of the line.
    - color (tuple): A tuple of RGB values for the line color.
    - layer (str): Which layer to draw the line on ("static" or "dynamic").
    """
    if layer == "static":
        pygame.draw.line(level_surface, color, (x1, y1), (x2, y2))  # Draw on static surface
    elif layer == "dynamic":
        pygame.draw.line(dynamic_surface, color, (x1, y1), (x2, y2))  # Draw on dynamic surface
    else:
        print("Error: Invalid layer specified. Use 'static' or 'dynamic'.")





# To store the keys being pressed
keys_pressed = []

keys_pressed = []

def snapshot_input():
    """
    Returns a snapshot of the keys that are currently pressed, updating continuously
    while a key is held down. It works for every key on the keyboard.
    """
    global keys_pressed

    # Poll for all pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        
        if event.type == pygame.KEYDOWN:  # A key is pressed
            key_name = pygame.key.name(event.key)
            if key_name not in keys_pressed:  # Avoid duplicate key presses
                keys_pressed.append(key_name)
        
        elif event.type == pygame.KEYUP:  # A key is released
            key_name = pygame.key.name(event.key)
            if key_name in keys_pressed:  # Remove the key from the pressed list
                keys_pressed.remove(key_name)

    # Return all keys that are currently pressed
    return tuple(keys_pressed)  # Return as a tuple of keys



def key_input():
    """
    Check for any key press and return the name of the key pressed.
    Returns:
    - (str): The name of the key pressed (e.g., 'a', 'space', etc.).
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        if event.type == pygame.KEYDOWN:
            return pygame.key.name(event.key)
    return ""

level_surface = pygame.Surface((CHATTER_WIDTH, CHATTER_HEIGHT))  # Static layer (background/level)
dynamic_surface = pygame.Surface((CHATTER_WIDTH, CHATTER_HEIGHT))  # Dynamic layer (moving objects)


def clear(color, layer="dynamic"):
    """
    Clears the specified layer with the given color.

    Args:
    - color (tuple): The color to fill the layer with (e.g., (0, 0, 0) for black).
    - layer (str): The layer to clear ("static" or "dynamic"). Default is "dynamic".
    """
    if layer == "static":
        level_surface.fill(color)  # Clear the static layer (level)
    elif layer == "dynamic":
        dynamic_surface.fill(color)  # Clear the dynamic layer (objects)
    else:
        print("Error: Invalid layer specified. Use 'static' or 'dynamic'.")


def get_mouse_position():
    """
    Get the current mouse position (X, Y).
    Returns:
    - (tuple): A tuple containing the current mouse position (X, Y).
    """
    return pygame.mouse.get_pos()

def get_mouse_state():
    """
    Get the state of the mouse (clicking and scrolling).
    Returns:
    - (dict): A dictionary with keys:
        - 'left_click': Boolean indicating if the left mouse button was clicked.
        - 'right_click': Boolean indicating if the right mouse button was clicked.
        - 'scroll_up': Boolean indicating if the scroll wheel was scrolled up.
        - 'scroll_down': Boolean indicating if the scroll wheel was scrolled down.
    """
    mouse_state = {
        'left_click': False,
        'right_click': False,
        'scroll_up': False,
        'scroll_down': False
    }

    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[0]:
        mouse_state['left_click'] = True

    if mouse_buttons[2]:
        mouse_state['right_click'] = True

    for event in pygame.event.get():

        if event.type == pygame.MOUSEWHEEL:

            if event.y > 0:
                mouse_state['scroll_up'] = True

            elif event.y < 0:
                mouse_state['scroll_down'] = True

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 4:
                mouse_state['scroll_up'] = True

            elif event.button == 5:
                mouse_state['scroll_down'] = True

    return mouse_state

# Initialize joystick
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
    print("No joystick detected!")


