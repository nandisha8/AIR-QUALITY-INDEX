function detectPollution() {
    // Simulated pollution level (random number between 0 and 100)
    var pollutionLevel = Math.floor(Math.random() * 101);
  
    // Display pollution level
    var levelDisplay = document.getElementById("level");
    levelDisplay.textContent = pollutionLevel;
  
    // Evaluate pollution level
    if (pollutionLevel >= 0 && pollutionLevel <= 30) {
      alert("Air quality is good!");
    } else if (pollutionLevel > 30 && pollutionLevel <= 60) {
      alert("Air quality is moderate.");
    } else if (pollutionLevel > 60 && pollutionLevel <= 90) {
      alert("Air quality is unhealthy.");
    } else {
      alert("Air quality is hazardous!");
    }
  
    // Update chart with new data point
    updateChart(pollutionLevel);
  }
  
  var chartData = {
    labels: [],
    datasets: [{
      label: 'Pollution Level',
      data: [],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }]
  };
  
  var ctx = document.getElementById('pollutionChart').getContext('2d');
  var pollutionChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  
  function updateChart(pollutionLevel) {
    var timeNow = new Date().toLocaleTimeString();
    chartData.labels.push(timeNow);
    chartData.datasets[0].data.push(pollutionLevel);
  
    // Keep only the last 10 data points for better visualization
    if (chartData.labels.length > 10) {
      chartData.labels.shift();
      chartData.datasets[0].data.shift();
    }
  
    pollutionChart.update();
  }