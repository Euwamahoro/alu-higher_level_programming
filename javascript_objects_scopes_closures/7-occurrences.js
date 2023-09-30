#!/usr/bin/node 

exports.nbOccurences = function (list, searchElement){
    num_occurences = 0;
    for (const element of list){
        if (element === searchElement){
            num_occurences += 1;
        }
    }
    return num_occurences;
}