# Colors

<svg viewBox="0 0 620 140" xmlns="http://www.w3.org/2000/svg">
  <!-- Neutrals -->
  <rect x="0" y="0" width="40" height="40" fill="#ffffff" stroke="#ccc" stroke-width="1"/>
  <rect x="40" y="0" width="40" height="40" fill="#f5f5f5"/>
  <rect x="80" y="0" width="40" height="40" fill="#c7cfcc"/>
  <rect x="120" y="0" width="40" height="40" fill="#819796"/>
  <rect x="160" y="0" width="40" height="40" fill="#577277"/>
  <rect x="200" y="0" width="40" height="40" fill="#253a5e"/>
  <rect x="240" y="0" width="40" height="40" fill="#172038"/>
  <!-- Blues -->
  <rect x="300" y="0" width="40" height="40" fill="#73bed3"/>
  <rect x="340" y="0" width="40" height="40" fill="#4f8fba"/>
  <rect x="380" y="0" width="40" height="40" fill="#3c5e8b"/>
  <rect x="420" y="0" width="40" height="40" fill="#29adff"/>
  <!-- Greens -->
  <rect x="0" y="50" width="40" height="40" fill="#0ced6a"/>
  <rect x="40" y="50" width="40" height="40" fill="#00d74e"/>
  <rect x="80" y="50" width="40" height="40" fill="#008f17"/>
  <!-- Ambers -->
  <rect x="140" y="50" width="40" height="40" fill="#ffcf45"/>
  <rect x="180" y="50" width="40" height="40" fill="#ffbd2c"/>
  <rect x="220" y="50" width="40" height="40" fill="#d37800"/>
  <!-- Reds -->
  <rect x="280" y="50" width="40" height="40" fill="#ff8680"/>
  <rect x="320" y="50" width="40" height="40" fill="#ff5a5b"/>
  <rect x="360" y="50" width="40" height="40" fill="#c62a34"/>
  <!-- Cyans -->
  <rect x="420" y="50" width="40" height="40" fill="#d7f0ef"/>
  <rect x="460" y="50" width="40" height="40" fill="#a8edea"/>
  <rect x="500" y="50" width="40" height="40" fill="#39dcd5"/>
  <!-- Pinks -->
  <rect x="560" y="50" width="40" height="40" fill="#f9eff2"/>
  <rect x="600" y="50" width="20" height="40" fill="#fed6e3"/>
  <rect x="560" y="0" width="40" height="40" fill="#fed6e3"/>
  <rect x="600" y="0" width="20" height="40" fill="#f07da2"/>
  <!-- Button Grays -->
  <rect x="480" y="0" width="25" height="40" fill="#e8e8e8"/>
  <rect x="505" y="0" width="25" height="40" fill="#e0e0e0"/>
  <rect x="530" y="0" width="25" height="40" fill="#d8d8d8"/>
  <!-- Labels -->
  <text x="120" y="110" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">neutrals</text>
  <text x="360" y="110" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">blues</text>
  <text x="505" y="110" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">grays</text>
  <text x="40" y="135" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">greens</text>
  <text x="180" y="135" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">ambers</text>
  <text x="320" y="135" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">reds</text>
  <text x="460" y="135" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">cyans</text>
  <text x="580" y="135" font-family="system-ui,sans-serif" font-size="9" fill="#577277" text-anchor="middle">pinks</text>
</svg>

## Rationale

The Frutiger Aero aesthetic emerged between 2004 and 2013 as a visual language of technological optimism. Where Y2K design expressed anxiety about the digital future, Frutiger Aero proposed a utopia: nature and technology in harmony, glass and light, the sky meeting the machine. The color system presented here attempts to capture that spirit while remaining practical for implementation.

Three principles govern the palette. First, colors must feel luminous—as if lit from within or behind, like a backlit display or sunlight through water. Second, the system must be systematic: no magic numbers, no one-off hex values scattered through stylesheets. Every color derives from a small set of primitives, combined through a quantized alpha scale. Third, the palette must be perceptually balanced. A red button and a green button should feel equally bright. This requires moving beyond RGB thinking into perceptually uniform color spaces.

The architecture follows modern design token conventions. Primitive tokens define the raw pigments. Semantic tokens assign meaning—what is text, what is accent, what is danger. Component tokens specify usage—the exact gradient on a pressed button. This separation means a dark theme requires only remapping semantic tokens; the component definitions remain unchanged.

## The Primitives

The base palette contains twelve colors plus two gradient anchors, derived primarily from the Apollo and PICO-8 palettes with adjustments for the Aqua/Aero aesthetic.

The neutral scale runs from pure white `#ffffff` through offwhite `#f5f5f5` to silver `#c7cfcc`, then through a cool gray `#819796` and a warmer gray-teal `#577277`, finally arriving at the near-black navy `#172038` used for primary text. This progression is not strictly linear in lightness; it curves through subtle hue shifts, picking up green-blue undertones in the midtones that prevent the grays from feeling dead or purely industrial. The darkest value `#172038` reads as black in most contexts but reveals deep blue when placed against true black, lending warmth to text-heavy interfaces.

The blue family serves as the primary accent. The base blue `#4f8fba` sits at moderate saturation—vivid enough to draw attention, muted enough to avoid overwhelming. Its lighter variant `#73bed3` shifts slightly toward cyan for hover states and highlights. The darker variant `#3c5e8b` provides pressed states and borders. A fourth blue, the bright `#29adff`, exists for moments requiring maximum emphasis: primary call-to-action buttons, active selections, links that must not be missed. This bright blue pushes toward the edge of the sRGB gamut without crossing into the garish.

The traffic light colors demand special care. Users have strong learned associations with red, amber, and green, and these colors must feel equally prominent despite their different hues. The solution involves tuning each triad—light, base, and dark variants—to approximately equal perceptual lightness. Green runs from `#0ced6a` through `#00d74e` to `#008f17`. Amber spans `#ffcf45` to `#ffbd2c` to `#d37800`. Red moves from `#ff8680` through `#ff5a5b` to `#c62a34`. When rendered as glossy buttons with the standard gradient treatment, these three colors command equal visual weight.

The cyan and pink families define the signature Frutiger Aero atmosphere. Cyan `#a8edea` and pink `#fed6e3` combine in a 135-degree diagonal gradient to produce the characteristic sky-meets-sunrise background. This pairing is not arbitrary: cyan sits at the boundary between green and blue, evoking water and clear sky, while pink occupies the warm rose range of dawn light. Together they suggest a world where technology exists within nature rather than against it. Each color now has light and dark variants, making them usable beyond the background gradient—as accent colors, highlights, or semantic tokens in their own right.

## The Alpha Scale

Transparency in this system is quantized to six steps: 10%, 25%, 50%, 75%, 90%, and 95%. This constraint prevents the proliferation of arbitrary alpha values and creates visual rhythm. A 10% overlay barely tints. A 25% wash provides subtle coloration. At 50% the overlay and background contribute equally. 75% reads as dominant but translucent—the classic frosted glass. 90% approaches opacity while retaining a hint of what lies beneath. 95% is glass: technically transparent, perceptually solid.

White alphas handle highlights, glass effects, and light overlays. The full set: `rgba(255,255,255,0.95)` for glass panels, `rgba(255,255,255,0.90)` for border highlights, `rgba(255,255,255,0.75)` for frosted surfaces, `rgba(255,255,255,0.50)` for content area backgrounds, `rgba(255,255,255,0.25)` for subtle washes, and `rgba(255,255,255,0.10)` for the faintest overlays.

Black alphas handle shadows and borders. The set is sparser: `rgba(0,0,0,0.50)` for text shadows requiring real weight, `rgba(0,0,0,0.25)` for drop shadows, `rgba(0,0,0,0.10)` for borders and subtle depth, and `rgba(0,0,0,0.05)` for the gentlest panel shadows. Two colored alphas exist for specific highlighting needs: a 10% blue for matched tag backgrounds and a 10% red for error line markers.

## Semantic Mapping

Text colors form a four-level hierarchy. Primary text uses the near-black navy `#172038`, providing strong contrast without the harshness of pure black. Muted text uses the warm gray-teal `#577277` for secondary information, labels, and supporting copy. Faint text drops to cool gray `#819796` for tertiary content, timestamps, and disabled states. Inverse text is pure white `#ffffff` for use on dark or colored backgrounds.

Backgrounds rely heavily on the alpha scale applied over the teal-peach gradient. Glass panels use 75% white alpha. Content areas use 50% white alpha. Headers employ a subtle vertical gradient from white to offwhite, creating the brushed-metal toolbar appearance characteristic of the era. The gutter—the line-number column in code editors—uses 95% white alpha, nearly opaque but retaining connection to the underlying gradient.

The accent system maps directly to the blue family. The primary accent is the base blue. Hover states use the dark blue. Borders and focus rings use navy. This creates a coherent interactive vocabulary: everything clickable shares a color family, with state changes expressed through value shifts rather than hue changes.

## Gradient Recipes

Frutiger Aero buttons are not flat. They simulate three-dimensional forms lit from above through careful gradient construction.

The default button gradient runs from pure white at the top to a mid-gray `#e0e0e0` at the bottom. This creates the illusion of a convex surface catching overhead light. On hover, the bottom color lightens to `#e8e8e8`, as if the button has lifted slightly toward the light source. On press, the gradient inverts: darker `#d8d8d8` at top, lighter `#e8e8e8` at bottom, simulating a surface pushed away from the light.

Accent buttons follow the same logic with color. The default runs from base blue to dark blue. Hover reverses the expectation, running from light blue to base blue—brighter overall, suggesting increased energy. The pressed state returns darkness to the top.

A shine pseudo-element overlays every glossy button: a 75% white alpha gradient from top to transparent at the midpoint. This highlight, inset slightly from the button edges, creates the characteristic Aqua "wet" appearance. On press, the shine flips to the bottom and reduces to 25% alpha, maintaining the lighting model.

Traffic light buttons receive the same treatment: light variant to base variant as the gradient, with the dark variant as the border. The shine overlay applies universally. The result is a set of colored buttons that feel like physical objects—gummy, tactile, pressable.

## Perceptual Notes

The traffic light colors were selected to achieve approximate perceptual balance. In the OKLCH color space, where L represents perceptual lightness independent of hue, the base values cluster around L=0.70-0.75. This means a row of red, amber, and green buttons will not have one color jumping out as brighter or duller than the others. The effect is subtle but important for interfaces where these colors appear together frequently.

The blue accent family was tuned to avoid the notorious blue-shift problem in LCH color spaces, where adjusting lightness or chroma causes unexpected hue drift. OKLCH corrects this issue, and the blue variants here move cleanly along the lightness axis without wandering toward purple or cyan.

The cyan-pink pairing was chosen for maximum emotional range within a harmonious pair. Cyan at `#a8edea` sits at approximately 177° hue—the boundary between green and blue, evoking both foliage and water. Pink at `#fed6e3` sits near 340°—the rose range, suggesting warmth without aggression. A 135-degree gradient between them sweeps through the cool-to-warm spectrum, creating a background that feels alive and atmospheric rather than static. The light and dark variants extend each color's utility: cyan-dark `#39dcd5` can serve as a secondary accent or success-adjacent highlight, while pink-dark `#f07da2` works for romantic or attention-seeking contexts distinct from the error-coded reds.

## Reference

### Neutrals

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-white` | `#ffffff` | Pure white. The top of every gradient, the shine on every button. |
| `--c-offwhite` | `#f5f5f5` | A whisper off white. Header gradient terminus, subtle differentiation. |
| `--c-silver` | `#c7cfcc` | Gray with a breath of green. Disabled states, decorative borders. |
| `--c-gray` | `#819796` | Cool mid-gray. Tertiary text, timestamps, the quiet parts of an interface. |
| `--c-gray-warm` | `#577277` | Gray pulling toward teal. Secondary text, labels, muted UI. |
| `--c-dark` | `#172038` | Near-black with hidden navy. Primary text, maximum contrast without harshness. |
| `--c-navy` | `#253a5e` | Deep blue. Accent borders, focus rings, the shadow beneath the surface. |

### Blues

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-blue` | `#4f8fba` | The workhorse accent. Links, selections, active states. |
| `--c-blue-light` | `#73bed3` | Lifted toward cyan. Hover states, highlights, the top of accent gradients. |
| `--c-blue-dark` | `#3c5e8b` | Pressed into shadow. Button press states, gradient bottoms. |
| `--c-blue-bright` | `#29adff` | Maximum emphasis. Primary CTAs, the color that demands action. |

### Greens

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-green` | `#00d74e` | Base green. Success, confirmation, go. |
| `--c-green-light` | `#0ced6a` | Electric highlight. Gradient top, hover glow. |
| `--c-green-dark` | `#008f17` | Forest shadow. Borders, pressed states. |

### Ambers

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-amber` | `#ffbd2c` | Base amber. Warning, caution, pause. |
| `--c-amber-light` | `#ffcf45` | Sunlit highlight. Gradient top, attention without alarm. |
| `--c-amber-dark` | `#d37800` | Burnt orange shadow. Borders, pressed states. |

### Reds

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-red` | `#ff5a5b` | Base red. Error, danger, stop. |
| `--c-red-light` | `#ff8680` | Softened alarm. Gradient top, hover warmth. |
| `--c-red-dark` | `#c62a34` | Deep warning. Borders, pressed states, blood under the skin. |

### Cyans

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-cyan` | `#a8edea` | Shallow water, morning sky. The optimistic side of technology. |
| `--c-cyan-light` | `#d7f0ef` | Mist on glass. Highlights, subtle tints. |
| `--c-cyan-dark` | `#39dcd5` | Tropical depth. Pressed states, emphasis. |

### Pinks

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-pink` | `#fed6e3` | Cherry blossom, dawn light. The human side of the machine. |
| `--c-pink-light` | `#f9eff2` | Barely there blush. Backgrounds, whispers of warmth. |
| `--c-pink-dark` | `#f07da2` | Rose in shadow. Accents, Valentine emphasis. |

### Button Grays

| Token | Hex | Description |
|-------|-----|-------------|
| `--c-btn-light` | `#e8e8e8` | Hover bottom. The button rises toward light. |
| `--c-btn-mid` | `#e0e0e0` | Default bottom. Neutral, waiting. |
| `--c-btn-dark` | `#d8d8d8` | Pressed top. The button sinks from light. |

### White Alphas

| Token | Value | Description |
|-------|-------|-------------|
| `--alpha-white-95` | `rgba(255,255,255,0.95)` | Glass. Nearly solid, barely breathing. |
| `--alpha-white-90` | `rgba(255,255,255,0.90)` | Border highlight. The edge catching light. |
| `--alpha-white-75` | `rgba(255,255,255,0.75)` | Frosted glass. The canonical translucency. |
| `--alpha-white-50` | `rgba(255,255,255,0.50)` | Half-veil. Content areas, equal presence. |
| `--alpha-white-25` | `rgba(255,255,255,0.25)` | Wash. A tint, a suggestion. |
| `--alpha-white-10` | `rgba(255,255,255,0.10)` | Breath. Barely there, felt more than seen. |

### Black Alphas

| Token | Value | Description |
|-------|-------|-------------|
| `--alpha-black-50` | `rgba(0,0,0,0.50)` | Heavy shadow. Text shadows that anchor. |
| `--alpha-black-25` | `rgba(0,0,0,0.25)` | Drop shadow. The standard depth cue. |
| `--alpha-black-10` | `rgba(0,0,0,0.10)` | Subtle border. Separation without weight. |
| `--alpha-black-05` | `rgba(0,0,0,0.05)` | Whisper shadow. Panels floating, barely. |

### Colored Alphas

| Token | Value | Description |
|-------|-------|-------------|
| `--alpha-blue-10` | `rgba(79,143,186,0.10)` | Selection tint. Matched tags, highlighted regions. |
| `--alpha-red-10` | `rgba(255,90,91,0.10)` | Error tint. The line where something went wrong. |

## Implementation

All colors should be defined as CSS custom properties on `:root`. Primitives use the `--c-` prefix. Alpha values use the `--alpha-` prefix. Semantic tokens reference primitives through `var()`. Component tokens reference semantic tokens. No hex value should appear outside the primitive definitions.

This architecture permits future migration to OKLCH syntax as browser support matures. The primitives can be redefined in OKLCH while semantic and component tokens remain unchanged. It also permits theming: a dark mode requires only redefining the semantic layer to point at different primitives or inverted alpha scales.

The system as specified targets the sRGB color space. The bright blue `#29adff` and the vivid greens approach but do not exceed sRGB boundaries. For displays supporting Display P3, the chroma values could be increased by approximately 30% to take advantage of the wider gamut, but this is not required for the aesthetic to function.
