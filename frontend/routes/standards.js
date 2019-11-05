var express = require('express');
var axios = require('axios');
var router = express.Router();

router.get("/browser", function(req, res) {
    res.render("standards/browser");
})

router.get("/:id", function(req, res) {
    res.render("standards/show", req.params)
})

module.exports = router;