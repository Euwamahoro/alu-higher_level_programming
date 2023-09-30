#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 && h <= 0) {
      // Create an empty object
      return;
    }
      // Initialize width and height attributes
      this.width = w;
      this.height = h;
  }
}

module.exports = Rectangle;
