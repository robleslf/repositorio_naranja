function getRandomInRange(min, max) {
  return Math.random() * (max - min) + min;
}

function calculateApproximateSum(num1, num2, minError, maxError) {
  const sum = num1 + num2;
  const error = getRandomInRange(minError, maxError);
  return sum + error;
}

const num1 = parseFloat(prompt("Introduce el primer número:"));
const num2 = parseFloat(prompt("Introduce el segundo número:"));

const minError = -1;  // Rango de error mínimo
const maxError = 2;   // Rango de error máximo

const result = calculateApproximateSum(num1, num2, minError, maxError);
console.log(`La suma más o menos sería: ${result.toFixed(2)}`);
