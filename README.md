# Fill_Pixel_Based_GivenSeed
Design and implement an algorithm to ‘fill’ a given pixel-based line drawing given a seed point.
You are limited to the Python Standard Library for this question. Do NOT use any external
libraries such as NumPy.
Design and implement an algorithm filling a two-dimensional image based on the seed point
given. If the seed point is inside a shape, you have to fill the whole shape.
Your program can take two input arguments:
• An image is a two-dimensional nested list representation of an image (see Figure 1
below)
• Seed point is a tuple (row, col) of the seed point to start filling. You may assume that
elements in the input image consist only of the integers 0 or 1, where
o 0 corresponds to an unfilled pixel
o 1 corresponds to a boundary pixel (a drawn ‘line’)

The function should fill the given image with the integer 2, starting from the seed point and
extending to its enclosing boundary (i.e. until it encounters 1).
The function should return a copy of the filled image. For example, the image in Figure 1a is
represented by the following list:
original_image = [[0, 0, 0, 0, 0, 0],
[1 , 0, 1 , 1 , 1 , 0],
[0, 1 , 0, 0, 0, 1 ],
[0, 0, 1 , 1 , 1 , 0],
[0, 0, 0, 0, 0, 0]]

Giving a seed point (2, 4) to your code, you should return the following list:
filled_image = [[0, 0, 0, 0, 0, 0],
[1 , 0, 1 , 1 , 1 , 0],
[0, 1 , 2, 2, 2, 1 ],
[0, 0, 1 , 1 , 1 , 0],
[0, 0, 0, 0, 0, 0]]

Two more examples are shown in the following figures. The code should return the
original image when an invalid seed point is given. For example, seed point=(6, 2) is an invalid
input for the example above, as this seed point is outside of the image.
