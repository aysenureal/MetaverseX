// character.rs

pub enum CharacterMode {
    Serious,      // Ciddi
    Emojis,       // Emojilerle yanıt
    Random,       // Rastgele ve gülme ifadeleri için yanıt
    Cynical,      // Alaycı ve Esprili
}

pub struct Bot {
    pub name: String,
    pub character_mode: CharacterMode,
}

impl Bot {
    pub fn new(name: &str, character_mode: CharacterMode) -> Self {
        Bot {
            name: name.to_string(),
            character_mode,
        }
    }

    pub fn change_mode(&mut self, new_mode: CharacterMode) {
        self.character_mode = new_mode;
    }

    pub fn respond(&self, message: &str) -> String {
        match self.character_mode {
            CharacterMode::Serious => format!("🤖 Let's stay serious: {}", message),
            CharacterMode::Emojis => {
                let emoji_response = message.chars().filter(|&c| c == '😊' || c == '😂' || c == '😎').collect::<String>();
                format!("{} {}", emoji_response, message)
            },
            CharacterMode::Random => {
                if message.contains("haha") || message.contains("ahahaha") || message.contains("hahahaha") {
                    // Rastgele yazı ya da gülme ifadelerine uygun cevap
                    format!("Haha, bunu ben de seviyorum! 😂 {}", message)
                } else {
                    // Diğer rastgele tepkiler
                    let random_responses = vec![
                        "Wow, interesting!",
                        "Okay, let's see...",
                        "Hmm... 🤔",
                        "Did you just say that?",
                    ];
                    format!("{}: {}", random_responses[rand::random::<usize>() % random_responses.len()], message)
                }
            },
            CharacterMode::Cynical => format!("😏 Oh, really? Here's the deal: {}", message),
        }
    }
}
