var country = "Australia";

/* global Plotly */
var url =
  `http://127.0.0.1:5000/api/v1/resources/electricity_production_values/country?id=${country}`;

/**
 * Helper function to select data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - country
 * index 1 - index
 * index 2 - percentage
 * index 3 - source_id
 * index 4 - year
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

function buildPlot() {
  d3.json(url).then(function(data) {

    // Grab values from the data json object to build the plots
    var country = data.dataset.country;
    var index = data.dataset.index;
    var percentage = data.dataset.percentage;
    var source_id = data.dataset.source_id['EG.ELC.FOSL.ZS'];
    var year = data.dataset.year;

    console.log(index[1]);

    // var trace1 = {
    //   type: "scatter",
    //   mode: "lines",
    //   name: name,
    //   x: dates,
    //   y: closingPrices,
    //   line: {
    //     color: "#17BECF"
    //   }
    // };

    // var data = [trace1];

    // var layout = {
    //   title: `${stock} closing prices`,
    //   xaxis: {
    //     range: [startDate, endDate],
    //     type: "date"
    //   },
    //   yaxis: {
    //     autorange: true,
    //     type: "linear"
    //   }
    // };

    // Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();
