# Generative Pixel Glow

This is my first generative-art project made using Python, NumPy, and Matplotlib.

I wanted to understand how an image can be created using pixels, mathematics, and programming instead of manually drawing a shape.

## What I Created

The program generates a 100 × 100 RGB image.

For every pixel, the program calculates its distance from the center and converts that distance into brightness.

The result is a glowing circular pattern generated completely by mathematical rules.

## How It Works

The main idea is:

Pixel position
→ distance from center
→ brightness
→ RGB value
→ image

The distance is calculated using the Pythagorean theorem:

H = √((x₂ − x₁)² + (y₂ − y₁)²)

I wanted the center to be brightest and the brightness to decrease as the distance increased.

So I used an inverse relationship:

Brightness = (255 × K) / H

I used K = 10 for the final version.

The center is handled separately because dividing by zero is not possible.

Brightness values are also limited to the RGB range of 0–255.

## RGB

Each pixel contains:

[Red, Green, Blue]

For this project I used:

[brightness, brightness, brightness]

Since all three values are equal, the image is grayscale.

## Experiments

I changed the value of K to see how the glow changed.

- K = 5 → smaller glow
- K = 10 → medium glow
- K = 20 → wider glow

This showed me how changing one mathematical parameter can affect thousands of pixels.

## What I Learned

- NumPy arrays
- RGB images
- Pixel coordinates
- Nested loops
- Euclidean distance
- Pythagorean theorem
- Inverse relationships
- RGB values and uint8
- Matplotlib image display
- Generative art
- Git and GitHub

## Files

- pixel_art.py — Python program that generates the image
- generative_glow.png — the generated image

## Technologies

- Python
- NumPy
- Matplotlib

## How to Run

Install NumPy and Matplotlib, then run:

```text
py pixel_art.py
