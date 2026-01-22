# AeroCode - Technical Report

## Overview

AeroCode is a CodePen-like code editor with a Frutiger Aero aesthetic. It features three resizable editor panels (HTML, CSS, JS) in a sidebar with a live preview pane.

## Architecture

### State Model

The application uses a declarative state model:

```javascript
state = {
    sidebarWidth: number,      // Current sidebar width in pixels
    prevSidebarWidth: number,  // Previous width (for restore after collapse)
    collapsed: boolean,        // Whether sidebar is collapsed to strip
    fullscreen: string|null,   // Which panel is fullscreen (or null)
    minimized: {               // Which panels are minimized
        html: boolean,
        css: boolean,
        js: boolean
    },
    heights: {                 // Panel heights when not minimized
        html: number,
        css: number,
        js: number
    }
}
```

### Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `MIN_H` | 28px | Minimum panel height (header-only when minimized) |
| `GAP` | 8px | Gap between panels and edges |
| `TOOLBAR_H` | 32px | Bottom toolbar height |
| `MIN_SIDEBAR_W` | 150px | Minimum sidebar width |
| `STRIP_W` | 16px | Width of collapsed sidebar strip |

### Rendering

The `render()` function is a pure derivation from state to DOM. It:
1. Handles sidebar collapsed/expanded state
2. Handles fullscreen mode
3. Positions panels based on their effective heights
4. Updates CodeMirror instances

## Panel Drag Behavior

### Key Design Decisions

1. **No Auto-Collapse**: Panels NEVER collapse automatically during drag. They stop at `MIN_H` and stay open.

2. **Click to Collapse**: Panels can only be minimized/restored by clicking the yellow traffic light button.

3. **Minimum Height Enforced**: All panels always maintain at least `MIN_H` (28px) height.

### Drag Algorithm

The `computeDragState(startState, draggedPanel, delta)` function computes the new state after a drag:

#### Dragging UP (delta < 0)
- Dragged panel grows
- Panels above shrink (closest first)
- Panels above stop at `MIN_H`, do not collapse
- Growth is limited by what can be taken from panels above

#### Dragging DOWN (delta > 0)
- Dragged panel shrinks (stops at `MIN_H`)
- Freed space goes to panels above
- If dragged panel is at `MIN_H`, leftover delta pushes panels below
- Pushed panels stop at `MIN_H`, do not collapse
- When CSS pushes JS, HTML grows to compensate (keeps CSS header tracking mouse)

### Constraints

The `enforceConstraints()` function ensures:
- Total panel heights fit within usable space
- All heights are at least `MIN_H`
- If overflow, panels shrink proportionally

## User Interactions

### Panel Headers
- **HTML header**: Click to toggle minimize (not draggable - nothing above it)
- **CSS/JS headers**: Drag to resize, click to toggle minimize

### Traffic Light Buttons
- **Yellow (minimize)**: Toggle panel minimize/restore
- **Green (fullscreen)**: Enter fullscreen mode for this panel
- **Red (exit)**: Exit fullscreen mode (only visible in fullscreen)

### Sidebar Resizing
- Drag right edge to resize
- Collapse to strip when width < 50px
- Snap to full width when near right edge
- Click strip to restore previous width

### Other Features
- **Copy button**: Copy panel content to clipboard
- **Share button**: Copy URL with compressed state to clipboard
- **Vim/Normal mode**: Toggle CodeMirror keymap
- **URL persistence**: State is compressed and stored in URL hash

## File Structure

```
22-aerocode/
├── pen.html      # Main application (self-contained)
└── report.md     # This documentation
```

## Dependencies

External (CDN-loaded):
- CodeMirror 5.65.13 (editor, modes, vim keymap)

## Code Organization

The JavaScript is organized into sections:

1. **Constants & Defaults** - Configuration and default code
2. **State** - Application state object
3. **Geometry Helpers** - Height calculations
4. **Constraint Enforcement** - Layout validation
5. **Render** - DOM updates from state
6. **Panel Actions** - Minimize/fullscreen logic
7. **Drag State Computation** - Pure function for drag behavior
8. **Event Binding** - User interaction handlers
9. **Preview & URL** - Live preview and sharing
10. **Initialization** - Startup sequence

## Testing

The drag logic was tested with a Node.js test shim verifying:
- No auto-collapse during any drag operation
- Minimum height always respected
- Correct space redistribution
- Edge cases (extreme drags, zero delta, minimized panels)

All 12 tests pass.

## Design Rationale

### Why No Auto-Collapse?

Auto-collapse during drag was confusing for users:
- Panels would disappear unexpectedly
- Hard to predict when collapse would occur
- Difficult to recover from accidental collapses

The new behavior is predictable: panels stay open and stop at their minimum height.

### Why Click-Only Collapse?

Explicit user action (clicking the yellow button) makes minimize/restore intentional and reversible. This follows the principle of least surprise.

### Why Compensate HTML When CSS Pushes JS?

Without compensation, the CSS header would lag behind the mouse when JS is being pushed. By growing HTML when JS shrinks, the CSS header stays aligned with the cursor position.

## Browser Compatibility

Tested in modern browsers supporting:
- CSS `backdrop-filter`
- CompressionStream/DecompressionStream API
- ES6+ features (arrow functions, template literals, async/await)
