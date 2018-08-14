import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
#from models import db_session, Department as DepartmentModel, Employee as EmployeeModel
from models import db_session, Staff as StaffModel

'''
■エンドポイント定義

・リクエスト例
{
  allDepartment {
    edges {
      node {
        id
      }
    }
  }
}
{
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}
class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )

class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee)
    all_department= SQLAlchemyConnectionField(Department)

schema = graphene.Schema(query=Query)
'''


'''
■エンドポイント定義

・リクエスト例
{
  allStaff {
    edges {
      node {
        id
        name
        branch
      }
    }
  }
}
'''
class Staff(SQLAlchemyObjectType):
    class Meta:
        model = StaffModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_staff = SQLAlchemyConnectionField(Staff)
    all_sample = SQLAlchemyConnectionField(Staff)

schema = graphene.Schema(query=Query)