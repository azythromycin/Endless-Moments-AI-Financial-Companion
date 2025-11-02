from fastapi import APIRouter, File, UploadFile, HTTPException
from smart_parser import smart_extract
import os

router = APIRouter(prefix="/parse", tags=["Parser"])


@router.post("/")
async def parse_any_file(file: UploadFile = File(...)):
    """Accepts image, PDF, or CSV and extracts text + structured info."""
    try:
        filename = file.filename
        temp_path = f"temp_{filename}"

        # Save file temporarily
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        # Run smart extraction
        result = smart_extract(temp_path)
        os.remove(temp_path)

        return {
            "filename": filename,
            "parsed_fields": result["parsed_fields"],
            "sample_text": result["raw_text"][:500]  # preview first 500 chars
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
