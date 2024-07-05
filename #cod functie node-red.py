#cod functie node-red
var payload = msg.payload;
var temperature = parseFloat(payload.temperature);
var pollution_index = parseFloat(payload.pollution_index);

var message= {
    topic: "/training/device/Elena-Gusatu/",
    payload: {
        temperature: temperature,
        pollution_index: pollution_index 
    },
    qos: 0,
    retain : false
};
return message;