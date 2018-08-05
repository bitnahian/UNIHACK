var file = cat('../data/geo/red_light_data.csv');
file = file.split('\n');
for(var i=1; i< file.length-1; i++){
    try{
    var line = file[i];
    line = line.split(','); 
     db.redFinal.insertOne ({locationCode: line[0], camera: line[1], locationDetails: line[2], schoolZone: line[3], redLight: line[4], count: parseFloat(line[5]) ,  location: { type: "Point", coordinates: [parseFloat(line[7]), parseFloat(line[6])]}});
    }
 catch (e){
	continue;
}
}
