var chalk = require('chalk'),
    GtfsRealtimeBindings = require('gtfs-realtime-bindings'),
    express = require('express'),
    path = require('path'),
    request = require('request'),
    app = express();

var requestSettings = {
    method: 'GET',
    url: 'URL OF YOUR GTFS-REALTIME SOURCE GOES HERE',
    encoding: null
};

/*
request(requestSettings, function (error, response, body) {
    if (!error && response.statusCode == 200) {
	var feed = GtfsRealtimeBindings.FeedMessage.decode(body);
	feed.entity.forEach(function(entity) {
	    if (entity.trip_update) {
		console.log(entity.trip_update);
	    }
	});
    }
});
*/

app.use(express.static(path.join(__dirname, '../public')))

app.get('/', function(req, res) {
    res.render('index.html');
});

app.listen(process.env.PORT || 7890);
console.log(chalk.yellow('Express server listening on port', process.env.PORT || 7890));
