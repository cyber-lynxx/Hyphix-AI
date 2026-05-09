let socket = io()
let current_id = null

function submit() {
  let chat_input = document.getElementById("chat_input")
  let responses = document.getElementById("responses")
  let message = chat_input.value
  if (message.length < 1) {return}
  chat_input.value = ""
  chat_input.disabled = true


  let bubble = document.createElement("p")
  bubble.className = "user_message"
  bubble.setHTML(message)
  responses.append(bubble)
  socket.emit("chat_send", message, current_id)
}

function enter(event) {
  if (event.key != "Enter") {return}
  submit()
}

function response(text, id) {
  current_id = id
  let bubble = document.createElement("p")
  bubble.className = "response_message"
  let responses = document.getElementById("responses")
  bubble.setHTML(text)
  responses.append(bubble)
  let chat_input = document.getElementById("chat_input")
  chat_input.disabled = false
}

socket.on("chat_response", response)
