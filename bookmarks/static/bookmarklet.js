if (typeof jQuery == 'undefined') {
	var jQ = document.createElement('script');
	jQ.type = 'text/javascript';
	jQ.onload=runthis;
	jQ.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js';
	document.body.appendChild(jQ);
} else {
	runthis();
}

function runthis() {
	// your JavaScript code goes here!
	var title = document.title;
	var location = document.location;
	var url = 'http://127.0.0.1:8000/add?title='+encodeURI(title)+'&url='+encodeURI(location)+'&k=1';
	$("body").append("<iframe src='"+url+"' style='display:none;'></iframe>");

}