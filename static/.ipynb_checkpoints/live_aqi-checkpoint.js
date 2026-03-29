const locationData = {
    "Gujarat": [
        {n:"Ahmedabad", lat:23.02, lon:72.57},
        {n:"Vadodara", lat:22.30, lon:73.20}
    ]
};

const stateSel = document.getElementById("stateSelect");

Object.keys(locationData).forEach(state => {
    let opt = document.createElement("option");
    opt.value = state;
    opt.innerHTML = state;
    stateSel.appendChild(opt);
});

function updateCities() {
    const state = stateSel.value;
    const citySelect = document.getElementById("citySelect");
    citySelect.innerHTML = '<option>Select City</option>';

    locationData[state].forEach(city => {
        let opt = document.createElement("option");
        opt.value = JSON.stringify(city);
        opt.innerHTML = city.n;
        citySelect.appendChild(opt);
    });
}

async function fetchDetailedAQI() {
    alert("Working 👍");
}

/* Chart */
const ctx = document.getElementById('trendChart');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['6AM','9AM','12PM','3PM','6PM','9PM'],
        datasets: [{
            label: 'AQI',
            data: [75, 82, 95, 110, 105, 90]
        }]
    }
});