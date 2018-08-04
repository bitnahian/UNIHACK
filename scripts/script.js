var file = cat('UNIHACK/data/geo/speed_data.csv');
file = file.split('\n');
for(var i=1; i< 10; i++){
    var line = file[i];
    line = line.split(','); 
     db.speed1.insertOne ({locationCode: line[0], camera: line[3], locationDetails: line[4], schoolZone: line[5], speedIndicator: line[6], count: parseFloat(line[7]) ,  location: { type: "Point", coordinates: [parseFloat(line[2]), parseFloat(line[1])]}});
    
}
