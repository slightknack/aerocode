from colormath.color_objects import sRGBColor, LabColor, LCHabColor
from colormath.color_conversions import convert_color

def hex_to_lch(hex_color):
    """Convert hex to LCH (Lightness, Chroma, Hue)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    rgb = sRGBColor(r, g, b)
    lch = convert_color(rgb, LCHabColor)
    return lch.lch_l, lch.lch_c, lch.lch_h

def lch_to_hex(l, c, h):
    """Convert LCH to hex"""
    lch = LCHabColor(l, c, h)
    rgb = convert_color(lch, sRGBColor)
    # Clamp values
    r = max(0, min(1, rgb.rgb_r))
    g = max(0, min(1, rgb.rgb_g))
    b = max(0, min(1, rgb.rgb_b))
    return '#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255))

# Current traffic light colors
print("=== Current Traffic Light Analysis ===")
colors = {
    'red': '#ff004d',
    'red-light': '#ff6b7a', 
    'yellow': '#ffec27',
    'yellow-light': '#ffef5c',
    'green': '#00e436',
    'green-light': '#3cef5c',
}

for name, hex_c in colors.items():
    l, c, h = hex_to_lch(hex_c)
    print(f"{name:12} {hex_c} -> L:{l:5.1f} C:{c:5.1f} H:{h:5.1f}")

print("\n=== Proposed Improvements ===")

# Red - keep the cherry hue but increase lightness for hover
red_l, red_c, red_h = hex_to_lch('#ff004d')
print(f"\nRed base: L={red_l:.1f}, C={red_c:.1f}, H={red_h:.1f}")
# Brighter red for hover - increase L more significantly
red_hover = lch_to_hex(min(red_l + 15, 85), red_c * 0.9, red_h)
print(f"Red hover (brighter): {red_hover}")

# Yellow - shift hue toward amber (lower hue = more orange/amber)
yellow_l, yellow_c, yellow_h = hex_to_lch('#ffec27')
print(f"\nYellow base: L={yellow_l:.1f}, C={yellow_c:.1f}, H={yellow_h:.1f}")
# Amber is around hue 70-80 (orange-yellow)
amber_base = lch_to_hex(88, 90, 75)  # More amber
amber_light = lch_to_hex(92, 85, 78)  # Lighter amber for hover
print(f"Amber base: {amber_base}")
print(f"Amber light: {amber_light}")

# Green - keep as is, its good
green_l, green_c, green_h = hex_to_lch('#00e436')
print(f"\nGreen base: L={green_l:.1f}, C={green_c:.1f}, H={green_h:.1f}")

# Blue for share button - use Apollo palette blue
print("\n=== Blue for Share Button ===")
blues = ['#4f8fba', '#73bed3', '#29adff', '#3c5e8b']
for b in blues:
    l, c, h = hex_to_lch(b)
    print(f"{b} -> L:{l:5.1f} C:{c:5.1f} H:{h:5.1f}")

# Propose a vibrant blue similar to PICO-8 blue
pico_blue = '#29adff'
l, c, h = hex_to_lch(pico_blue)
blue_dark = lch_to_hex(l - 15, c, h)
blue_light = lch_to_hex(min(l + 10, 90), c * 0.9, h)
print(f"\nShare button blue: {pico_blue}")
print(f"Share hover (lighter): {blue_light}")
print(f"Share border (darker): {blue_dark}")

# Generate complete traffic light palette with matching brightness
print("\n=== Final Recommended Palette ===")
# All at similar perceptual lightness for consistency
base_L = 65  # Good visible lightness
hover_L = 78  # Brighter for hover
pressed_L = 55  # Darker for pressed

# Hues: Red ~30, Amber ~70, Green ~145
print("\nTraffic Red (cherry):")
print(f"  base:    {lch_to_hex(base_L, 80, 30)}")
print(f"  light:   {lch_to_hex(hover_L, 75, 30)}")
print(f"  border:  {lch_to_hex(45, 70, 30)}")

print("\nTraffic Amber:")
print(f"  base:    {lch_to_hex(base_L + 20, 85, 70)}")  # Yellow is naturally lighter
print(f"  light:   {lch_to_hex(hover_L + 12, 80, 73)}")
print(f"  border:  {lch_to_hex(60, 75, 65)}")

print("\nTraffic Green:")
print(f"  base:    {lch_to_hex(base_L + 10, 90, 145)}")
print(f"  light:   {lch_to_hex(hover_L + 5, 85, 145)}")
print(f"  border:  {lch_to_hex(50, 80, 145)}")

print("\nShare Blue (PICO-8 style):")
print(f"  base:    {lch_to_hex(65, 50, 255)}")
print(f"  light:   {lch_to_hex(75, 45, 255)}")
print(f"  border:  {lch_to_hex(45, 55, 255)}")
