import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function GameUI() {
  const [question, setQuestion] = useState(null);
  const [answer, setAnswer] = useState(null);
  const [result, setResult] = useState(null);

  useEffect(() => {
    fetch("/api/get-question")
      .then((res) => res.json())
      .then((data) => setQuestion(data.question));
  }, []);

  const handleAnswer = (userAnswer) => {
    setAnswer(userAnswer);
    fetch("/api/submit-answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answer: userAnswer }),
    })
      .then((res) => res.json())
      .then((data) => setResult(data.result));
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-4">
      <Card className="w-full max-w-lg text-center">
        <CardContent className="p-6">
          {question ? (
            <>
              <motion.h2 className="text-2xl font-bold mb-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>{question}</motion.h2>
              <div className="flex justify-center gap-4">
                <Button onClick={() => handleAnswer("yes")} className="bg-green-500">Evet</Button>
                <Button onClick={() => handleAnswer("no")} className="bg-red-500">Hayır</Button>
              </div>
            </>
          ) : (
            <p>Yükleniyor...</p>
          )}
          {result && <p className="mt-4 text-xl">{result}</p>}
        </CardContent>
      </Card>
    </div>
  );
}
