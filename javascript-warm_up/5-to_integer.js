#!/usr/bin/node

const firstArg = process.argv[2];
if (/^-?\d+$/.test(firstArg)) {
    const intValue = parseInt(firstArg);
    console.log(`My number: ${intValue}`);
} else {
    console.log('Not a number');
}
