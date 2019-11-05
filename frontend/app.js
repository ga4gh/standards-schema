var express = require('express'),
    bodyParser = require('body-parser');

var standardsRoutes = require("./routes/standards");

var app = express();
app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use("/standards", standardsRoutes);
app.listen(3001, '0.0.0.0', function() {
    console.log("server has started");
})