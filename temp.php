
<?php

$url = "/home/pi/Documents/daten.json"; // path to your JSON file
$data = file_get_contents($url); // put the contents of the file into a variable
$characters = json_decode($data); // decode the JSON feed

//echo $characters[0]->time;

foreach ($characters as $character) {
	echo $character->time;
	echo " ";
	echo $character->temp;
	echo "C ";
	$druck = $character->druck;
	$ausgabe = $druck/100; 
	echo round($ausgabe,2);
	//echo $character->druck/100;
	echo "hPa" . '<br>';
	//echo $character->temp;
	//echo "C" . '<br>';
}

?>
