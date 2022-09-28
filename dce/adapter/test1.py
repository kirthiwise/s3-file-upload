
always() &&
      needs.detect-file-changes.outputs.datalake == 'true' &&
      github.event.push == true &&
      ((needs.deploy-frontend.result == 'success' || needs.deploy-frontend.result == 'skipped') ||
      (needs.deploy-backend.result == 'success' || needs.deploy-backend.result == 'skipped'))

      sadfdsf