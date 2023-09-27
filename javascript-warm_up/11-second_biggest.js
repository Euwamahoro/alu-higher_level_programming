#!/usr/bin/node

if (process.argv.length === 3) {
    console.log(0);
} else if (process.argv.length > 3) {
    let maxNumber = parseInt(process.argv[2]);
    for (let i = 3; i < process.argv.length; i++) {
        const currentNumber = parseInt(process.argv[i]);
        if (currentNumber > maxNumber) {
            maxNumber = currentNumber;
        }
    }
    console.log(maxNumber);}
