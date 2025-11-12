const chatEl = document.getElementById('chat');
const form = document.getElementById('chat-form');
const input = document.getElementById('message');
let history = [];

function addMessage(role, content){
  const row = document.createElement('div');
  row.className = `msg ${role}`;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.textContent = content;
  row.appendChild(bubble);
  chatEl.appendChild(row);
  chatEl.scrollTop = chatEl.scrollHeight;
}

window.addEventListener('DOMContentLoaded', async () => {
  addMessage('assistant', 'Welkom bij Facilicom 👋 — ik ben de Facilicom Chatbot. Waarmee kan ik je vandaag helpen?');
  try {
    const res = await fetch('/health');
    document.getElementById('status').textContent = res.ok ? 'verbonden' : 'offline';
  } catch { document.getElementById('status').textContent = 'offline'; }
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if(!text) return;
  input.value = '';
  addMessage('user', text);
  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, history })
    });
    if(!res.ok) throw new Error(await res.text());
    const data = await res.json();
    addMessage('assistant', data.reply);
    history.push({ role:'user', content:text });
    history.push({ role:'assistant', content:data.reply });
  } catch (err){
    console.error(err);
    addMessage('assistant', 'Er ging iets mis. Controleer de server en probeer opnieuw.');
    document.getElementById('status').textContent = 'offline';
  }
});
