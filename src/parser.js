const fs = require('fs');
const path = require('path');

function parseFile(filePath) {
  try {
    const fileBuffer = fs.readFileSync(filePath);
    const fileContent = fileBuffer.toString();
    return fileContent;
  } catch (error) {
    const errorMessage = `Error parsing file at ${filePath}: ${error.message}`;
    console.error(errorMessage);
    throw new Error(errorMessage);
  }
}

function parseCsv(filePath) {
  try {
    const fileContent = parseFile(filePath);
    const rows = fileContent.split('\n');
    const data = rows.map((row) => row.split(','));
    return data;
  } catch (error) {
    throw new Error(`Error parsing CSV file at ${filePath}: ${error.message}`);
  }
}

function parseJson(filePath) {
  try {
    const fileContent = parseFile(filePath);
    return JSON.parse(fileContent);
  } catch (error) {
    throw new Error(`Error parsing JSON file at ${filePath}: ${error.message}`);
  }
}

module.exports = { parseFile, parseCsv, parseJson };