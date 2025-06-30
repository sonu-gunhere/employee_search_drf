from rest_framework.decorators import api_view
from rest_framework.response import Response

from emp_app.rate_limiter import rate_limit
from emp_app.serializers import EmployeeSerializer
from .data import EMPLOYEES, ORG_COLUMN_CONFIG



@api_view(['GET'])
@rate_limit
def employee_search(request):
    org_id = request.query_params.get('org_id')
    query = request.query_params.get('query', '').lower()
    status = request.query_params.get('status', '')
    location = request.query_params.get('location', '')
    company = request.query_params.get('company', '')
    department = request.query_params.get('department', '')
    position = request.query_params.get('position', '')

    config = ORG_COLUMN_CONFIG.get(org_id)
    if not config:
        return Response([])

    result = []
    for emp in EMPLOYEES:
        if emp["org_id"] != org_id:
            continue
        if query and query not in emp["name"].lower():
            continue
        if status and emp["status"] != status:
            continue
        if location and emp["location"] != location:
            continue
        if company and emp["company_id"] != company:
            continue
        if department and emp["department"] != department:
            continue
        if position and emp["position"] != position:
            continue

        filtered = {k: emp[k] for k in config if k != "company"}
        if "company" in config:
            filtered["company"] = emp["company_id"]
        result.append(filtered)

    serializer = EmployeeSerializer(result, many=True)
    return Response(serializer.data)